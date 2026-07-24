"use client";

type Props = {
  filters: any;
  selectedFilters: any;
  setSelectedFilters: any;
};

export default function Filters({
  filters,
  selectedFilters,
  setSelectedFilters,
}: Props) {
  if (!filters) return null;

  return (
    <div className="bg-gray-800 rounded-xl p-6 mb-8">

      <h2 className="text-2xl font-bold mb-6">
        Filters
      </h2>

      <div className="grid grid-cols-4 gap-5">

        {Object.keys(filters).map((column) => (

          <div key={column}>

            <label className="block mb-2">
              {column}
            </label>

            <select
              value={selectedFilters[column] || ""}
              onChange={(e) =>
                setSelectedFilters({
                  ...selectedFilters,
                  [column]: e.target.value,
                })
              }
              className="w-full bg-white text-black rounded px-4 py-2"
            >

              <option value="">
                All
              </option>

              {filters[column].map((value: string) => (

                <option
                  key={value}
                  value={value}
                >
                  {value}
                </option>

              ))}

            </select>

          </div>

        ))}

      </div>

    </div>
  );
}