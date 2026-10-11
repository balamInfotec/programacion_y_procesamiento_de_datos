import { useEffect, useRef } from "react";
import * as echarts from "echarts";

export default function GaugeChart({ value, metricName, min = 0, max = 100 }) {
  const chartRef = useRef(null);
  const chartInstance = useRef(null);

  useEffect(() => {
    if (!chartInstance.current) {
      chartInstance.current = echarts.init(chartRef.current);
    }

    const option = {
      backgroundColor: "transparent",
      series: [
        {
          type: "gauge",
          min,
          max,
          progress: {
            show: true,
            width: 10
          },
          axisLine: {
            lineStyle: {
              width: 10
            }
          },
          axisLabel: {
            color: "#ccc"
          },
          pointer: {
            width: 4
          },
          detail: {
            valueAnimation: true,
            formatter: "{value}",
            color: "#fff",
            fontSize: 20
          },
          title: {
            color: "#fff",
            fontSize: 16
          },
          data: [
            {
              value,
              name: metricName
            }
          ]
        }
      ]
    };

    chartInstance.current.setOption(option);
  }, [value]);

  return (
    <div
      ref={chartRef}
      className="w-full h-64 bg-slate-800 rounded-lg"
    />
  );
}
