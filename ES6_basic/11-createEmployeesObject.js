export default function createEmployeesObject(departmentName, employees) {
  const propertyName = `${departmentName}`;
  const employeesObject = {
    [propertyName]: employees
  };

  return employeesObject;
}
