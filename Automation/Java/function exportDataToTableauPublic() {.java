function exportDataToTableauPublic() {
  var spreadsheetId = '1JIfIdIEkDEQdZQXQDe_49TszZygJ1Y2PSmWW3R4PDhk';
  var sheetNames = ['DJI', 'NDX', 'SPX', 'Nat Gasx3', 'biotechx3', 'Healthx3', 'SPXL', 'UDOW', 'UPRO', 'FAS', 'RETL', 'SOXL', 'TNA', 'TQQQ', 'TECL', 'rusell'];
  var folderId = '1QsaKDijcR3r-jz6a1UaFEyo9WZvSjImM'; // Replace with the ID of the folder where you want to save the CSV files
  
  var folder = DriveApp.getFolderById(folderId);
  
  for (var i = 0; i < sheetNames.length; i++) {
    var sheetName = sheetNames[i];
    var sheet = SpreadsheetApp.openById(spreadsheetId).getSheetByName(sheetName);
    var dataRange = sheet.getDataRange();
    var data = dataRange.getValues();
    var csvData = convertToCsv(data);
    var fileName = sheetName + '.csv';
    var file = folder.createFile(fileName, csvData);
  }
  
  Logger.log('Data exported successfully!');
}

function convertToCsv(data) {
  var csv = '';
  
  for (var row = 0; row < data.length; row++) {
    for (var col = 0; col < data[row].length; col++) {
      var cellValue = data[row][col].toString();
      if (cellValue.includes(',')) {
        cellValue = '"' + cellValue + '"';
      }
      csv += cellValue;
      if (col < data[row].length - 1) {
        csv += ',';
      }
    }
    csv += '\n';
  }
  
  return csv;
}
