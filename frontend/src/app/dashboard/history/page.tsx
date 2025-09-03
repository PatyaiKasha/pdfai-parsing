import { HistoryTable } from "@/components/features/HistoryTable";

export default function HistoryPage() {
  return (
    <div>
      <div className="mb-8">
        <h1 className="text-2xl font-bold text-gray-900">Job History</h1>
        <p className="mt-2 text-gray-600">
          View the status and results of your past and current parsing jobs.
        </p>
      </div>
      <HistoryTable />
    </div>
  );
}
