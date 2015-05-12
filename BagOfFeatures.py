import cv2  
import numpy as np
 
class BagOfFeatures:
    """This is a class of Bag-of-Features by K-means for OpenCV"""
    codebookSize=0
    classifier=None
    def __init__(self, codebookSize):
        self.codebookSize=codebookSize
        self.classifier=cv2.KNearest()
        
    def train(self,features,iterMax=100,term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )):
        retval, bestLabels, codebook=cv2.kmeans(features,self.codebookSize,term_crit,iterMax,cv2.KMEANS_RANDOM_CENTERS)
        self.classifier.train(codebook,np.array(range(self.codebookSize)))
        
    def makeHistogram(self, feature):
        histogram=np.zeros(self.codebookSize)
        if self.classifier==None :
            raise Exception("You need train this instance.")
        retval, results, neighborResponses, dists=self.classifier.find_nearest(feature,1)
        for idx in results:
            idx=int(idx)
            histogram[idx]=histogram[idx]+1
        histogram=cv2.normalize(histogram,norm_type=cv2.NORM_L2)
        #transpose
        histogram=np.reshape(histogram,(1,-1))
        return histogram

