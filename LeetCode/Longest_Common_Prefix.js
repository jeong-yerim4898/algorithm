const longestCommonPrefix = function(strs) {
  if (!strs.length) return "";
  
  const standard = strs[0];
  
  for (let i = 0; i < standard.length; i++) {
      const prefix = standard.slice(0, standard.length - i);
      
      for (let j = 0;j < strs.length; j++) {
          if (!strs[j].startsWith(prefix)) {
              break;
          }
          if (j === strs.length - 1) {
              return prefix;
          }
      }
  }
  return "";
};