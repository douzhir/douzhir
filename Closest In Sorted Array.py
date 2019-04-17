class Solution(object):
  def closest(self, array, target):
    if not array:
      return -1
    left = 0
    right = len(array) - 1
    while left < right-1:
      mid = (left + right)/2
      if array[mid] > target:
        right = mid
      elif array[mid] < target:
        left = mid
      else:
        return mid
    return left if abs(array[left]-target)<abs(array[right]-target) else right
