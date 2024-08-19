class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
      if len(haystack) -len(needle)<0:
          return -1

      i =0
      while i <= len(haystack) -len(needle):
          if needle == haystack[i : i + len(needle)]:
              return i
          i = i+1
      return -1
