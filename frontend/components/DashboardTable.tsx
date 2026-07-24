"use client";

type Props = {
  chartData: any[];
};

export default function DashboardTable({ chartData }: Props) {
  if (!chartData || chartData.length === 0) {
    return (
      <div className="bg-gray-800 rounded-xl p-8 mt-8 text-center">
        <h2 className="text-2xl font-bold text-white">
          No Data Available
        </h2>

        <p className="text-gray-400 mt-3">
          Generate a dashboard to display the data table.
        </p>
      </div>
    );
  }

  const columns = Object.keys(chartData[0]);

  return (
    <div className="bg-gray-800 rounded-xl p-8 mt-8 shadow-lg">

      <div className="flex justify-between items-center mb-6">

        <h2 className="text-3xl font-bold text-white">
          Dashboard Table
        </h2>

        <span className="bg-blue-600 px-4 py-2 rounded-lg text-sm">
          {chartData.length} Records
        </span>

      </div>

      <div className="overflow-x-auto overflow-y-auto max-h-[500px] rounded-lg border border-gray-700">

        <table className="min-w-full border-collapse">

          <thead className="sticky top-0 bg-gray-700">

            <tr>

              <th className="border border-gray-600 px-4 py-3 text-left">
                #
              </th>

              {columns.map((column) => (
                <th
                  key={column}
                  className="border border-gray-600 px-4 py-3 text-left"
                >
                  {column}
                </th>
              ))}

            </tr>

          </thead>

          <tbody>

            {chartData.map((row, index) => (

              <tr
                key={index}
                className={
                  index % 2 === 0
                    ? "bg-gray-900 hover:bg-gray-700"
                    : "bg-gray-800 hover:bg-gray-700"
                }
              >

                <td className="border border-gray-700 px-4 py-3">
                  {index + 1}
                </td>

                {columns.map((column) => (

                  <td
                    key={column}
                    className="border border-gray-700 px-4 py-3"
                  >
                    {String(row[column])}
                  </td>

                ))}

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
}