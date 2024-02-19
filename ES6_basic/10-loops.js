export default function appendToEachArrayValue(array, appendString) {
  for (const idx of array) {
    const NewArray = [];
    NewArray = appendString + idx;
  }

  return NewArray;
}
