export default function appendToEachArrayValue(array, appendString) {
  for (const idx of array) {
    const NewArray = [];
    NewArray.push(appendString + idx);
  }

  return NewArray;
}
