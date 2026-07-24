"use client";

import {
    ResponsiveContainer,
    CartesianGrid,
    Tooltip,
    Legend,
    XAxis,
    YAxis,
    BarChart,
    Bar,
    LineChart,
    Line,
    PieChart,
    Pie,
    Cell,
    ScatterChart,
    Scatter,
} from "recharts";

interface Props {
    chart: any;
}

const COLORS = [
    "#3B82F6",
    "#06B6D4",
    "#10B981",
    "#F59E0B",
    "#EF4444",
    "#8B5CF6",
    "#EC4899",
    "#84CC16",
];

export default function ChartRenderer({ chart }: Props) {

    const tooltipStyle = {
        backgroundColor: "#111827",
        border: "1px solid #334155",
        borderRadius: "12px",
        color: "#fff",
    };

    switch (chart.type) {

        //-------------------------------- BAR --------------------------------//

        case "bar":

            return (

                <ResponsiveContainer width="100%" height={380}>

                    <BarChart
                        data={chart.data}
                        margin={{ top: 20, right: 30, left: 20, bottom: 20 }}
                    >

                        <defs>

                            <linearGradient id="barGradient" x1="0" y1="0" x2="0" y2="1">

                                <stop offset="0%" stopColor="#3B82F6"/>

                                <stop offset="100%" stopColor="#06B6D4"/>

                            </linearGradient>

                        </defs>

                        <CartesianGrid
                            strokeDasharray="4 4"
                            stroke="#334155"
                        />

                        <XAxis
                            dataKey={chart.x}
                            tick={{ fill:"#CBD5E1", fontSize:12 }}
                        />

                        <YAxis
                            tick={{ fill:"#CBD5E1", fontSize:12 }}
                        />

                        <Tooltip contentStyle={tooltipStyle}/>

                        <Legend/>

                        <Bar
                            dataKey={chart.y}
                            fill="url(#barGradient)"
                            radius={[10,10,0,0]}
                            animationDuration={1200}
                        />

                    </BarChart>

                </ResponsiveContainer>

            );

        //-------------------------------- LINE --------------------------------//

        case "line":

            return (

                <ResponsiveContainer width="100%" height={380}>

                    <LineChart
                        data={chart.data}
                        margin={{ top:20,right:30,left:20,bottom:20 }}
                    >

                        <CartesianGrid
                            strokeDasharray="4 4"
                            stroke="#334155"
                        />

                        <XAxis
                            dataKey={chart.x}
                            tick={{ fill:"#CBD5E1" }}
                        />

                        <YAxis
                            tick={{ fill:"#CBD5E1" }}
                        />

                        <Tooltip contentStyle={tooltipStyle}/>

                        <Legend/>

                        <Line
                            type="monotone"
                            dataKey={chart.y}
                            stroke="#10B981"
                            strokeWidth={4}
                            dot={{
                                r:5,
                                stroke:"#10B981",
                                strokeWidth:2,
                                fill:"#fff"
                            }}
                            activeDot={{
                                r:8
                            }}
                            animationDuration={1500}
                        />

                    </LineChart>

                </ResponsiveContainer>

            );

        //-------------------------------- PIE --------------------------------//

        case "pie":

            return (

                <ResponsiveContainer width="100%" height={420}>

                    <PieChart>

                        <Pie
                            data={chart.data}
                            dataKey={chart.values}
                            nameKey={chart.labels}
                            outerRadius={145}
                            innerRadius={70}
                            paddingAngle={5}
                            label
                            animationDuration={1400}
                        >

                            {

                                chart.data.map((_:any,index:number)=>(

                                    <Cell
                                        key={index}
                                        fill={COLORS[index % COLORS.length]}
                                        stroke="#111827"
                                        strokeWidth={2}
                                    />

                                ))

                            }

                        </Pie>

                        <Tooltip contentStyle={tooltipStyle}/>

                        <Legend/>

                    </PieChart>

                </ResponsiveContainer>

            );

        //-------------------------------- SCATTER --------------------------------//

        case "scatter":

            return (

                <ResponsiveContainer width="100%" height={380}>

                    <ScatterChart
                        margin={{ top:20,right:20,left:20,bottom:20 }}
                    >

                        <CartesianGrid
                            stroke="#334155"
                            strokeDasharray="4 4"
                        />

                        <XAxis
                            dataKey={chart.x}
                            tick={{ fill:"#CBD5E1" }}
                        />

                        <YAxis
                            dataKey={chart.y}
                            tick={{ fill:"#CBD5E1" }}
                        />

                        <Tooltip contentStyle={tooltipStyle}/>

                        <Legend/>

                        <Scatter
                            data={chart.data}
                            fill="#8B5CF6"
                        />

                    </ScatterChart>

                </ResponsiveContainer>

            );

            case "horizontalBar":

    return (

        <ResponsiveContainer width="100%" height={350}>

            <BarChart
                layout="vertical"
                data={chart.data}
                margin={{
                    top: 20,
                    right: 30,
                    left: 80,
                    bottom: 20,
                }}
            >

                <XAxis
                    type="number"
                />

                <YAxis
                    type="category"
                    dataKey={chart.y}
                    width={120}
                />

                <Tooltip />

                <Bar
                    dataKey={chart.x}
                    fill="#3B82F6"
                    radius={[0,8,8,0]}
                />

            </BarChart>

        </ResponsiveContainer>

    );

        default:
            return null;

    }

}