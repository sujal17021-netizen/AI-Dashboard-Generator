export default function Sidebar() {
  const menus = [
    "📊 Dashboard",
    "📁 Upload",
    "📈 Analytics",
    "📉 Charts",
    "📋 Reports",
    "📥 Export",
    "⚙ Settings",
  ];

  return (
    <aside className="w-64 min-h-screen bg-gray-950 text-white p-6">
      <h2 className="text-3xl font-bold mb-10">
        Excel BI
      </h2>

      <ul className="space-y-5">
        {menus.map((menu) => (
          <li
            key={menu}
            className="cursor-pointer rounded-lg p-3 hover:bg-blue-600 transition"
          >
            {menu}
          </li>
        ))}
      </ul>
    </aside>
  );
}