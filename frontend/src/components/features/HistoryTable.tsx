"use client";

import { useEffect, useState } from "react";
import api from "@/lib/api";
import { ParseJob } from "@/lib/types";
import { format } from "date-fns";
import { JobStatusBadge } from "./JobStatus";

export function HistoryTable() {
  const [jobs, setJobs] = useState<ParseJob[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchHistory = async () => {
      try {
        const response = await api.get<ParseJob[]>("/users/history");
        setJobs(response.data);
      } catch (err) {
        setError("Failed to load job history.");
      } finally {
        setIsLoading(false);
      }
    };

    fetchHistory();
  }, []);

  if (isLoading) return <p>Loading history...</p>;
  if (error) return <p className="text-red-600">{error}</p>;

  if (jobs.length === 0) {
    return (
      <div className="text-center mt-10">
        <h3 className="text-lg font-medium text-gray-900">No jobs found</h3>
        <p className="text-sm text-gray-500">Upload a PDF to get started.</p>
      </div>
    )
  }

  return (
    <div className="mt-8 flow-root">
      <div className="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div className="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
          <div className="overflow-hidden shadow ring-1 ring-black ring-opacity-5 rounded-lg">
            <table className="min-w-full divide-y divide-gray-300">
              <thead className="bg-gray-50">
                <tr>
                  <th scope="col" className="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6">Filename</th>
                  <th scope="col" className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Status</th>
                  <th scope="col" className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Created At</th>
                  <th scope="col" className="relative py-3.5 pl-3 pr-4 sm:pr-6">
                    <span className="sr-only">View</span>
                  </th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-200 bg-white">
                {jobs.map((job) => (
                  <tr key={job.id}>
                    <td className="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6">{job.filename}</td>
                    <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                      <JobStatusBadge status={job.status} />
                    </td>
                    <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">{format(new Date(job.created_at), "PPP p")}</td>
                    <td className="relative whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-6">
                      <a href="#" className="text-aurora-600 hover:text-aurora-900">View Details</a>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}
