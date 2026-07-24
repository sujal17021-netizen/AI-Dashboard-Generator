type Props = {
  prompt: string;
  setPrompt: (value: string) => void;

  file: File | null;
  setFile: (file: File | null) => void;

  generateDashboard: () => void;
};

export default function DashboardGenerator({

  prompt,

  setPrompt,

  file,

  setFile,

  generateDashboard,

}: Props) {

  return (

    <div className="bg-gray-900 rounded-2xl p-10 shadow-xl">

      <h1 className="text-4xl font-bold mb-2">
        🤖 AI Dashboard Generator
      </h1>

      <p className="text-gray-400 mb-8">
        Upload an Excel file and describe the dashboard you want.
      </p>

      {/* Upload Area */}

      <label
        className="
        border-2
        border-dashed
        border-gray-600
        rounded-xl
        p-12
        flex
        flex-col
        justify-center
        items-center
        cursor-pointer
        hover:border-blue-500
        transition
        "
      >

        <span className="text-6xl">
          📎
        </span>

        <p className="mt-4 text-lg">
          {file ? file.name : "Click to upload an Excel file"}
        </p>

        <input
          hidden
          type="file"
          accept=".xlsx,.xls"
          onChange={(e) => {

            if (e.target.files) {

              setFile(e.target.files[0]);

            }

          }}
        />

      </label>

      {/* Prompt */}

      <textarea

        value={prompt}

        onChange={(e) => setPrompt(e.target.value)}

        placeholder="Generate dashboard"

        rows={3}

        className="w-full mt-8 rounded-xl p-5 text-black"

        onKeyDown={(e) => {

          if (e.key === "Enter" && !e.shiftKey) {

            e.preventDefault();

            generateDashboard();

          }

        }}

      />

      {/* Generate Button */}

      <button

        onClick={generateDashboard}

        className="mt-6 w-full bg-blue-600 hover:bg-blue-700 py-3 rounded-xl font-semibold transition"

      >

        🚀 Generate Dashboard

      </button>

    </div>

  );

}