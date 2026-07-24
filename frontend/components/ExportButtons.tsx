"use client";

import * as XLSX from "xlsx";
import { saveAs } from "file-saver";
import jsPDF from "jspdf";
import autoTable from "jspdf-autotable";

type Props = {
  chartData: any[];
};

export default function ExportButtons({ chartData }: Props) {
  if (!chartData || chartData.length === 0) {
    return null;
  }

  // --------------------------
  // Export Excel
  // --------------------------
  const exportExcel = () => {
    const worksheet = XLSX.utils.json_to_sheet(chartData);

    const workbook = XLSX.utils.book_new();

    XLSX.utils.book_append_sheet(
      workbook,
      worksheet,
      "Dashboard"
    );

    const excelBuffer = XLSX.write(workbook, {
      bookType: "xlsx",
      type: "array",
    });

    const blob = new Blob([excelBuffer], {
      type:
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    });

    saveAs(blob, "Dashboard.xlsx");
  };

  // --------------------------
  // Export CSV
  // --------------------------
  const exportCSV = () => {
    const worksheet = XLSX.utils.json_to_sheet(chartData);

    const csv = XLSX.utils.sheet_to_csv(worksheet);

    const blob = new Blob([csv], {
      type: "text/csv;charset=utf-8;",
    });

    saveAs(blob, "Dashboard.csv");
  };

  // --------------------------
  // Export PDF
  // --------------------------
  const exportPDF = () => {
    const doc = new jsPDF();

    const columns = Object.keys(chartData[0]);

    const rows = chartData.map((row) =>
      columns.map((col) => row[col])
    );

    doc.setFontSize(18);

    doc.text("Dashboard Report", 14, 20);

    autoTable(doc, {
      head: [columns],
      body: rows,
      startY: 30,
      theme: "grid",
      headStyles: {
        fillColor: [41, 128, 185],
      },
    });

    doc.save("Dashboard.pdf");
  };

  return (
    <div className="bg-gray-800 rounded-xl p-8 mt-8">

      <h2 className="text-2xl font-bold mb-6 text-white">
        Export Dashboard
      </h2>

      <div className="flex flex-wrap gap-5">

        <button
          onClick={exportExcel}
          className="bg-green-600 hover:bg-green-700 px-6 py-3 rounded-lg font-semibold"
        >
          📊 Export Excel
        </button>

        <button
          onClick={exportCSV}
          className="bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded-lg font-semibold"
        >
          📄 Export CSV
        </button>

        <button
          onClick={exportPDF}
          className="bg-red-600 hover:bg-red-700 px-6 py-3 rounded-lg font-semibold"
        >
          📕 Export PDF
        </button>

      </div>

    </div>
  );
}