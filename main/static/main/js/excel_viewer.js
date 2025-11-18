const excelViewer = document.getElementById('excelViewer');

function showTable(rawTable) {
    let reader = new FileReader();

    reader.addEventListener("loadend", (evt) => {
        excelViewer.innerHTML = "";

        let workbook = XLSX.read(evt.target.result, { type: "binary" });
        let worksheet = workbook.Sheets[workbook.SheetNames[0]];
        let range = XLSX.utils.decode_range(worksheet["!ref"]);

        for (let row = range.s.r; row <= range.e.r; row++) {
            let r = excelViewer.insertRow();
            for (let col = range.s.c; col <= range.e.c; col++) {
                let c = r.insertCell();
                let xcell = worksheet[XLSX.utils.encode_cell({ r: row, c: col })];
                c.innerHTML = xcell ? xcell.v : "";
            }
        }
    });

    reader.readAsBinaryString(rawTable);
}

function getFileFromServer(url) {
    let request = new XMLHttpRequest();

    request.open("GET", url);
    request.responseType = "blob";

    request.onload = function () {
        showTable(request.response);
    };

    request.send();
}