import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";

import { TelemetryProvider } from "./context/TelemetryContext";
import { LogsProvider } from "./context/LogsContext";
import { DeviceProvider } from "./context/DeviceContext";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <TelemetryProvider>
      <LogsProvider>
        <DeviceProvider>
          <App />
        </DeviceProvider>
      </LogsProvider>
    </TelemetryProvider>
  </React.StrictMode>
);
