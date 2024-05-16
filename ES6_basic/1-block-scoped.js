/*
Export a function with boolen values
*/

export default function taskBlock(trueOrFalse) {
    const task = false;
    const task2 = true;

    if (trueOrFalse) {
        const task = false;
        const task2 = true;

        return [task, task2]
    }

    return [task, task2];
}
