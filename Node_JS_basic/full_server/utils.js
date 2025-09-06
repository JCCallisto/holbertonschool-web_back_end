import fs from 'fs';

/**
 * Reads the database asynchronously.
 * @param {String} dataPath The path to the CSV data file.
 * @returns {Promise<{
 *   CS: String[],
 *   SWE: String[],
 * }>} Promise that resolves with the students grouped by field.
 */
const readDatabase = (dataPath) => new Promise((resolve, reject) => {
  fs.readFile(dataPath, 'utf-8', (err, data) => {
    if (err) {
      reject(err);
    } else {
      const fileLines = data
        .toString('utf-8')
        .trim()
        .split('\n');
      const studentGroups = {};
      const dbFieldNames = fileLines[0].split(',');
      const studentPropNames = dbFieldNames.slice(0, dbFieldNames.length - 1);

      for (const line of fileLines.slice(1)) {
        const studentRecord = line.split(',');
        const studentPropValues = studentRecord.slice(0, studentRecord.length - 1);
        const field = studentRecord[studentRecord.length - 1];
        if (!Object.keys(studentGroups).includes(field)) {
          studentGroups[field] = [];
        }
        const studentEntries = studentPropNames
          .map((propName, idx) => [propName, studentPropValues[idx]]);
        studentGroups[field].push(Object.fromEntries(studentEntries));
      }

      const students = {};
      for (const [field, group] of Object.entries(studentGroups)) {
        students[field] = group.map((student) => student.firstname);
      }
      resolve(students);
    }
  });
});

export default readDatabase;
