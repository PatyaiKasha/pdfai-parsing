import { FileUpload } from "@/components/features/FileUpload";

export default function UploadPage() {
  return (
    <div>
      <div className="mb-8">
        <h1 className="text-2xl font-bold text-gray-900">Upload a new PDF</h1>
        <p className="mt-2 text-gray-600">
          Drag and drop your file below to start the parsing process.
        </p>
      </div>
      <FileUpload />
    </div>
  );
}
