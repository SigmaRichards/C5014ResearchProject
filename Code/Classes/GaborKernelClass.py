from skimage.filters import gabor_kernel
import numpy as np
from scipy.signal import convolve

class GaborFeatures:
    def __init__(self):
        self.kernels = []
    
    def _log_kernels(self,kernelSize, num_orientations, num_scales):
        meshRange = np.arange(-kernelSize/2, kernelSize/2 + kernelSize%2)
        
        x, y = np.meshgrid(meshRange,meshRange)
        mid = np.where(np.logical_and(x==0,y==0))
        
        r = np.sqrt(x**2+y**2)
        r[mid] = 1
        rho = np.log2(r)
        theta = np.arctan2(y,x)
        
        scales = [a for a in range(num_scales)]
        
        #Orientation Component
        ts = np.asarray([[a + 0.5*((b+1)%2) for a in range(2*num_orientations)] for b in scales])
        theta_st = np.pi*ts/num_orientations
        
        #I don't really know how this works but it fixes the distortion
        costheta = np.cos(theta)
        sintheta = np.sin(theta)
        ds = [[sintheta * np.cos(c_angle) - costheta * np.sin(c_angle) for c_angle in c_scale] for c_scale in theta_st]  
        dc = [[costheta * np.cos(c_angle) + sintheta * np.sin(c_angle) for c_angle in c_scale] for c_scale in theta_st]
        dtheta = np.arctan2(ds,dc)
        
        sig_theta = 0.996*(np.pi/(np.sqrt(2)*num_orientations))
        
        orientation = np.exp(-0.5*((dtheta/sig_theta)**2))
        
        #Frequency Component
        rho_s = [np.log2(kernelSize)-a for a in range(num_scales)]
        sig_rho = 0.996*np.sqrt(2/3)
        
        frequency = [np.exp(-0.5*((rho-a)/sig_rho)**2) for a in rho_s]
        
        
        out = []
        for c_s in scales:
            for c_o in range(orientation.shape[1]):
                c_kern = frequency[c_s]*orientation[c_s,c_o]
                c_kern[mid] = 0
                out.append(c_kern)
            
        return np.asarray(out)
        
    
    def add_kernels(self,freqs,thetas,bands,stds,offs):
        kernels = []
        for freq in freqs:
            for theta in thetas:
                for band in bands:
                    for std in stds:
                        for off in offs:
                            kernel = np.real(gabor_kernel(frequency = freq,theta=theta,
                                                          bandwidth=band, n_stds = std,
                                                          offset = off))
                            kernels.append(kernel)
        self.kernels.extend(kernels)
    
    def add_log_kernels(self,kernelSize, num_orientations,num_scales):
        vals = [a for a in self._log_kernels(kernelSize,num_orientations,num_scales)]
        self.kernels.extend(vals)
    
    def convolve_kernels(self,img,layers = ["intensity"]):
        obj = []
        if "intensity" in layers:
            obj.append(np.max(img,axis=2))
        if "red" in layers:
            obj.append(img[:,:,0])
        if "green" in layers:
            obj.append(img[:,:,1])
        if "blue" in layers:
            obj.append(img[:,:,2])

        out = np.zeros((img.shape[0],img.shape[1],len(obj),len(self.kernels)))
        for i in range(len(self.kernels)):
            for l in range(len(obj)):
                out[:,:,l,i]=convolve(obj[l],self.kernels[i],mode="same")
        return out
