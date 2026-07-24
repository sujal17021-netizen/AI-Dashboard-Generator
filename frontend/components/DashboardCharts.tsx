"use client";

import ChartRenderer from "./ChartRenderer";

type Props = {
    charts: any[];
};

export default function DashboardCharts({ charts }: Props) {

    if (!charts || charts.length === 0) {

        return (
            <div className="text-white mt-10">
                No charts generated.
            </div>
        );
    }

    return (

    <div className="mt-10">

        <h1 className="text-4xl font-bold text-white mb-8">

            <div className="mb-10">

<h1 className="
text-5xl
font-black
tracking-tight
bg-gradient-to-r
from-cyan-400
via-blue-400
to-indigo-500
text-transparent
bg-clip-text
">

AI Dashboard

</h1>

<p className="text-slate-400 mt-2">

Generated automatically using AI

</p>

</div>

        </h1>

        <div className="grid grid-cols-1 xl:grid-cols-2 gap-8">

            {charts.map((chart, index) => (

                <div
                    key={index}
                    className="
                        bg-gradient-to-br
from-slate-900
to-slate-800
                        rounded-2xl
                        border
                        border-slate-600
                        shadow-2xl
shadow-cyan-500/20
                        p-6
                        hover:scale-[1.02]
                        hover:shadow-cyan-500/30
                        transition-all
                        duration-300
                        overflow-hidden
                    "
                >

                    <h2 className="text-2xl font-semibold text-white mb-6">

                        {chart.title}

                    </h2>

                    <ChartRenderer chart={chart} />

                </div>

            ))}

        </div>

    </div>

);
}