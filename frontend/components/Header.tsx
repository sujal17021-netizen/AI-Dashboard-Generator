export default function Header() {
  return (
    <div className="bg-gray-800 rounded-xl p-6 flex justify-between items-center mb-8">

      <div>
        <h1 className="text-3xl font-bold">
          Excel Analytics Dashboard
        </h1>

        <p className="text-gray-400">
          Interactive Business Intelligence Dashboard
        </p>
      </div>

      <div className="flex items-center gap-4">

        <input
          placeholder="Search..."
          className="px-4 py-2 rounded-lg text-black"
        />

        <div className="w-10 h-10 rounded-full bg-blue-600 flex items-center justify-center">
          👤
        </div>

      </div>

    </div>
  );
}