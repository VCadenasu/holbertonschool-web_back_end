/*
Export a function with boolen values
*/

export default function taskBlock(trueOrFalse) {
    let task = false;
    let task2 = true;

    if (trueOrFalse) {
        let task = false;
        let task2 = true;

        return [task, task2]
    }

    return [task, task2];
}
