import React from "react";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="flex h-screen bg-gray-50 font-sans">
      {/* Placeholder for Sidebar */}
      <div className="w-64 flex-shrink-0 bg-white border-r border-gray-200">
        <div className="p-4 border-b border-gray-200">
          <h1 className="text-xl font-bold text-aurora-700">AI PDF Parser</h1>
        </div>
        <nav className="mt-4 p-2">
          <a href="/dashboard" className="block px-4 py-2 rounded-lg text-gray-700 bg-aurora-100 font-semibold">Dashboard</a>
          <a href="/dashboard/upload" className="block px-4 py-2 rounded-lg text-gray-600 hover:bg-aurora-100 hover:text-gray-900">Upload</a>
          <a href="/dashboard/history" className="block px-4 py-2 rounded-lg text-gray-600 hover:bg-aurora-100 hover:text-gray-900">History</a>
          <a href="/dashboard/settings" className="block px-4 py-2 rounded-lg text-gray-600 hover:bg-aurora-100 hover:text-gray-900">Settings</a>
        </nav>
      </div>

      <div className="flex-1 flex flex-col overflow-hidden">
        {/* Placeholder for Header */}
        <header className="bg-white border-b border-gray-200 p-4">
          <div className="flex items-center justify-between">
            <h2 className="text-lg font-semibold text-gray-800">Overview</h2>
            {/* User Profile Dropdown Placeholder */}
            <div className="w-8 h-8 bg-aurora-200 rounded-full"></div>
          </div>
        </header>

        {/* Main Content */}
        <main className="flex-1 overflow-y-auto p-6">
          {children}
        </main>
      </div>
    </div>
  );
}
