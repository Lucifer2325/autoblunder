export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-6xl font-black tracking-tight mb-4 bg-gradient-to-r from-indigo-400 to-cyan-400 bg-clip-text text-transparent">
        Autoblunder
      </h1>
      <p className="text-lg text-slate-400 mb-8 max-w-md text-center">
        Generate, render, and schedule brainrot videos at scale.
      </p>
      <div className="flex gap-4">
        <button className="px-6 py-3 bg-indigo-600 hover:bg-indigo-500 rounded-lg font-bold transition">
          New Video
        </button>
        <button className="px-6 py-3 border border-slate-700 hover:border-slate-500 rounded-lg font-medium transition">
          View Dashboard
        </button>
      </div>
    </main>
  );
}
