import { cn } from "@/lib/utils";

type JobStatus = 'pending' | 'processing' | 'completed' | 'failed';

interface JobStatusBadgeProps {
  status: JobStatus;
  className?: string;
}

export function JobStatusBadge({ status, className }: JobStatusBadgeProps) {
  const statusText = status.charAt(0).toUpperCase() + status.slice(1);

  return (
    <span
      className={cn(
        "inline-flex items-center rounded-md px-2 py-1 text-xs font-medium",
        {
          "bg-green-100 text-green-800": status === "completed",
          "bg-yellow-100 text-yellow-800 animate-pulse": status === "processing",
          "bg-red-100 text-red-800": status === "failed",
          "bg-gray-100 text-gray-700": status === "pending",
        },
        className
      )}
    >
      <div className={cn(
        "h-2 w-2 rounded-full mr-2",
        {
          "bg-green-500": status === "completed",
          "bg-yellow-500": status === "processing",
          "bg-red-500": status === "failed",
          "bg-gray-500": status === "pending",
        }
      )} />
      {statusText}
    </span>
  );
}
