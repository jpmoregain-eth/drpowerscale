import ChatInterface from "@/components/ChatInterface";

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-[#001E2B] text-white shadow-lg">
        <div className="max-w-6xl mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                fill="currentColor"
                className="w-8 h-8 text-[#0076CE]"
              >
                <path d="M4 5h16a1 1 0 011 1v12a1 1 0 01-1 1H4a1 1 0 01-1-1V6a1 1 0 011-1zm0 2v10h16V7H4zm2 2h4v2H6V9zm0 4h4v2H6v-2zm6-4h6v2h-6V9zm0 4h6v2h-6v-2z" />
              </svg>
              <div>
                <h1 className="text-xl md:text-2xl font-bold tracking-tight">
                  Dr PowerScale
                </h1>
                <p className="text-sm text-blue-300 hidden sm:block">
                  AI-powered NAS & PowerScale / Isilon assistant
                </p>
              </div>
            </div>
            <div className="hidden md:flex items-center space-x-1 text-sm text-blue-300">
              <span className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></span>
              <span>Online</span>
            </div>
          </div>
        </div>
      </header>

      {/* Disclaimer Banner */}
      <div className="bg-amber-50 border-b border-amber-200">
        <div className="max-w-6xl mx-auto px-4 py-3">
          <div className="flex items-start space-x-2">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="currentColor"
              className="w-5 h-5 text-amber-600 flex-shrink-0 mt-0.5"
            >
              <path
                fillRule="evenodd"
                d="M9.401 3.003c1.155-2 4.043-2 5.197 0l7.355 12.748c1.154 2-.29 4.5-2.599 4.5H4.645c-2.309 0-3.752-2.5-2.598-4.5L9.4 3.003zM12 8.25a.75.75 0 01.75.75v3.75a.75.75 0 01-1.5 0V9a.75.75 0 01.75-.75zm0 8.25a.75.75 0 100-1.5.75.75 0 000 1.5z"
                clipRule="evenodd"
              />
            </svg>
            <p className="text-sm text-amber-800">
              <strong>Disclaimer:</strong> This is an AI-powered demonstration
              for Dell PowerScale / Isilon NAS storage queries. Not an official
              Dell Technologies product or support channel. For official
              support, please contact{" "}
              <a
                href="https://www.dell.com/support"
                className="underline font-medium"
                target="_blank"
                rel="noopener noreferrer"
              >
                Dell Support
              </a>
              .
            </p>
          </div>
        </div>
      </div>

      {/* Main Chat Area */}
      <main className="flex-1 flex flex-col max-w-4xl w-full mx-auto bg-gray-100">
        <ChatInterface />
      </main>

      {/* Footer */}
      <footer className="bg-[#001E2B] text-white py-4">
        <div className="max-w-6xl mx-auto px-4">
          <div className="flex flex-col md:flex-row items-center justify-between text-sm text-blue-300">
            <p>Dr PowerScale — AI Storage Assistant</p>
            <div className="flex items-center space-x-4 mt-2 md:mt-0">
              <span className="flex items-center space-x-1">
                <span className="text-green-400">●</span>
                <span>Powered by AI</span>
              </span>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}
