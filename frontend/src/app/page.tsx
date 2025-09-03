import Link from "next/link";

export default function HomePage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24 bg-aurora-50">
      <div className="text-center">
        <h1 className="text-4xl font-bold tracking-tight text-aurora-900 sm:text-6xl">
          AI PDF Parser
        </h1>
        <p className="mt-6 text-lg leading-8 text-aurora-700">
          Unlock structured data from your PDFs with the power of AI.
        </p>
        <div className="mt-10 flex items-center justify-center gap-x-6">
          <Link
            href="/dashboard"
            className="rounded-aurora bg-aurora-600 px-6 py-3 text-sm font-semibold text-white shadow-aurora hover:bg-aurora-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-aurora-600 transition-colors"
          >
            Get started
          </Link>
          <Link href="/login" className="text-sm font-semibold leading-6 text-gray-900">
            Log in <span aria-hidden="true">→</span>
          </Link>
        </div>
      </div>
    </main>
  );
}
