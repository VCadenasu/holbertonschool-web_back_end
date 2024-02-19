export default function appendToEachArrayValue(array, appendString) {
  for (const idx of array) {
    let NewArray;
    NewArray = appendString + idx;
  }

  return NewArray;
}
