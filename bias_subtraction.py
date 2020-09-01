"""
Created on Mon Aug 31 21:55:38 2020

@author: bikram
"""
def create_master_bias(frames):
  # Operations
  
  return master_bias

def bias_correct(frames):
  # Operations
  master_bias = create_master_bias(frames)
  for frame in frames:
    bias_corrected_frame = frame-master_bias
  
  return bias_corrected_frame
    
