import { useEffect, useRef } from "react";
import * as echarts from "echarts";

export default function RealtimeChart({ data, metricName }) {
  const chartRef = useRef(null);
  const chartInstance = useRef(null);

  useEffect(() => {
    if (!chartInstance.current) {
      chartInstance.current = echarts.init(chartRef.current);
    }

    const option = {
      backgroundColor: "transparent",
      title: {
        text: metricName,
        textStyle: { color: "#fff" }
      },
      tooltip: {
        trigger: "axis"
      },
      xAxis: {
        type: "category",
        data: data.map((d) => d.timestamp),
        axisLabel: { color: "#ccc" }
      },
      yAxis: {
        type: "value",
        axisLabel: { color: "#ccc" }
      },
      series: [
        {
          name: metricName,
          type: "line",
          smooth: true,
          showSymbol: false,
          data: data.map((d) => d.value),
          lineStyle: {
            color: "#4ade80",
            width: 2
          }
        }
      ]
    };

    chartInstance.current.setOption(option);
  }, [data]);

  return (
    <div
      ref={chartRef}
      className="w-full h-64 bg-slate-800 rounded-lg"
    />
  );
}
