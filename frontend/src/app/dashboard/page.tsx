export default function DashboardPage() {
  return (
    <div>
      <h1 className="text-2xl font-bold text-gray-900">Welcome to your Dashboard</h1>
      <p className="mt-2 text-gray-600">
        This is where you'll manage your documents, view parsing history, and see your usage.
      </p>
      <div className="mt-6 p-6 bg-white rounded-aurora border border-gray-200 shadow-sm">
        <h2 className="text-lg font-semibold text-aurora-700">Quick Start</h2>
        <p className="mt-2 text-gray-600">
          Navigate to the <a href="/dashboard/upload" className="text-aurora-600 font-medium hover:underline">Upload</a> page to parse your first PDF.
        </p>
      </div>
    </div>
  );
}
