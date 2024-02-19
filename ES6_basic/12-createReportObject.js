export default function createReportObject(employeesList) {
  const obs = {
    allEmployees: { ...employeesList },
    getNumberOfDepartments(employeesList) {
      return Object.keys(employeesList).length;
    },
  };

  return obs;
}
