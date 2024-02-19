export default function appendToEachArrayValue(array, appendString) {
  const NewArray = [];
  
  for (const idx of array) {
    NewArray = appendString + idx;
  }

  return NewArray;
}
