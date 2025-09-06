const express = require('express');
const fs = require('fs');

/**
 * Counts the students in a CSV data file asynchronously.
 * @param {String} dataPath The path to the CSV data file.
 */
const countStudents = (dataPath) => new Promise((resolve, reject) => {
  fs.readFile(dataPath, 'utf-8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
    }
    if (data) {
      const reportParts = [];
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

      const totalStudents = Object
        .values(studentGroups)
        .reduce((pre, cur) => (pre || []).length + cur.length);
      reportParts.push(`Number of students: ${totalStudents}`);
      for (const [field, group] of Object.entries(studentGroups)) {
        reportParts.push([
          `Number of students in ${field}: ${group.length}.`,
          `List: ${group.map((student) => student.firstname).join(', ')}`,
        ].join(' '));
      }
      resolve(reportParts.join('\n'));
    }
  });
});

/**
 * Creates a small Express server.
 */
const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const responseParts = ['This is the list of our students'];
  countStudents(process.argv[2])
    .then((report) => {
      responseParts.push(report);
      const responseText = responseParts.join('\n');
      res.send(responseText);
    })
    .catch((err) => {
      responseParts.push(err instanceof Error ? err.message : err.toString());
      const responseText = responseParts.join('\n');
      res.send(responseText);
    });
});

app.listen(1245);

module.exports = app;
