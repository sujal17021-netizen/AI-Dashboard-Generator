"use client";

import { useState } from "react";


import KPICards from "@/components/KPICards";
import DashboardCharts from "@/components/DashboardCharts";
import DashboardTable from "@/components/DashboardTable";
import ExportButtons from "@/components/ExportButtons";
import Sidebar from "@/components/Sidebar";
import Header from "@/components/Header";
import DashboardGenerator from "@/components/DashboardGenerator";
export default function Home() {
  const [file, setFile] = useState<File | null>(null);

  const [result, setResult] = useState<any>(null);


  const [tableData, setTableData] = useState<any[]>([]);


  const [insights, setInsights] = useState("");
  const [prompt, setPrompt] = useState("");
  const [datasetId, setDatasetId] = useState<number | null>(null);
  const [uploadedFileInfo, setUploadedFileInfo] = useState<{
    name: string;
    size: number;
    lastModified: number;
} | null>(null);

  //----------------------------------
  // Upload Excel
  //----------------------------------

  //----------------------------------
  // Generate Dashboard
  //----------------------------------

 const generateDashboard = async () => {

    try {

        let currentDatasetId = datasetId;

        // Upload automatically if user selected a file
        if (
    file &&
    (
        datasetId === null ||

        uploadedFileInfo === null ||

        uploadedFileInfo.name !== file.name ||

        uploadedFileInfo.size !== file.size ||

        uploadedFileInfo.lastModified !== file.lastModified
    )
) {

    currentDatasetId = await uploadDataset();

} {

    currentDatasetId = await uploadDataset();

}

        if (!currentDatasetId) {

            alert("No dataset available.");

            return;

        }

        const formData = new FormData();

        formData.append(
            "dataset_id",
            currentDatasetId.toString()
        );

        formData.append(
            "prompt",
            prompt
        );

        const response = await fetch(
            "https://dashboard-backend-rekb.onrender.com/dashboard/generate",
            {
                method: "POST",
                body: formData,
            }
        );

        const data = await response.json();

        console.log(data);

        setResult(data);

        setInsights(data.insights || "");

        setTableData(data.tableData || []);

    } catch (error) {

        console.error(error);

        alert("Failed to generate dashboard.");

    }

};

const uploadDataset = async (): Promise<number> => {

    if (!file) {
        throw new Error("Please select an Excel file.");
    }

    const formData = new FormData();

    formData.append("file", file);

    const response = await fetch(
        "https://dashboard-backend-rekb.onrender.com/dashboard/upload",
        {
            method: "POST",
            body: formData,
        }
    );

    const data = await response.json();

    setDatasetId(data.dataset_id);
    setUploadedFileInfo({
    name: file!.name,
    size: file!.size,
    lastModified: file!.lastModified,
});

    return data.dataset_id;
};
  //----------------------------------
  // UI
  //----------------------------------

  return (
    <div className="
min-h-screen
bg-gradient-to-br
from-slate-950
via-slate-900
to-slate-800
text-white
flex
">

      <Sidebar />

      <main className="flex-1 p-8">

        <Header />

        

        {result?.kpis && (
          <>
            <KPICards
              kpis={result.kpis}
            />
           
          </>
        )}
        <DashboardGenerator

    file={file}
    setFile={setFile}

    prompt={prompt}
    setPrompt={setPrompt}

  

    generateDashboard={generateDashboard}

/>

        {result && (

<DashboardCharts

    charts={result.charts}

/>

)}

        <DashboardTable
          chartData={tableData}
        />

        

        <ExportButtons
          chartData={tableData}
        />

      </main>

    </div>
  );
}