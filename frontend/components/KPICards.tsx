"use client";

interface KPI {

    title: string;

    value: number;

}

interface Props {

    kpis: KPI[];

}

const gradients = [

    "from-blue-600 to-cyan-500",

    "from-green-600 to-emerald-500",

    "from-purple-600 to-pink-500",

    "from-orange-500 to-red-500",

    "from-indigo-600 to-blue-500",

    "from-pink-600 to-purple-500",

];

const icons = [

    "📈",

    "💰",

    "📊",

    "📦",

    "🚀",

    "⭐",

];

export default function KPICards({ kpis }: Props) {

    if (!kpis || kpis.length === 0) {

        return null;

    }

    return (

        <div className="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-6 mb-10">

            {

                kpis.map((kpi, index) => (

                    <div

                        key={index}

                        className="
                        relative
                        overflow-hidden
                        rounded-3xl
                        bg-gradient-to-br
                        from-slate-900
                        to-slate-800
                        border
                        border-slate-700
                        shadow-xl
                        hover:shadow-cyan-500/30
                        hover:-translate-y-1
                        hover:scale-[1.03]
                        transition-all
                        duration-300
                        p-6
                        "

                    >

                        <div

                            className={`
                            absolute
                            -top-10
                            -right-10
                            w-32
                            h-32
                            rounded-full
                            blur-3xl
                            opacity-20
                            bg-gradient-to-r
                            ${gradients[index % gradients.length]}
                            `}

                        />

                        <div className="flex justify-between items-center">

                            <div>

                                <p className="text-slate-400 text-sm">

                                    {kpi.title}

                                </p>

                                <h2 className="text-4xl font-black mt-4 text-white">

                                    {Number(kpi.value).toLocaleString()}

                                </h2>

                            </div>

                            <div

                                className={`
                                w-16
                                h-16
                                rounded-2xl
                                flex
                                items-center
                                justify-center
                                text-3xl
                                bg-gradient-to-r
                                ${gradients[index % gradients.length]}
                                `}

                            >

                                {icons[index % icons.length]}

                            </div>

                        </div>

                        <div className="mt-8">

                            <div className="h-2 bg-slate-700 rounded-full">

                                <div

                                    className={`
                                    h-2
                                    rounded-full
                                    bg-gradient-to-r
                                    ${gradients[index % gradients.length]}
                                    w-4/5
                                    `}

                                />

                            </div>

                        </div>

                    </div>

                ))

            }

        </div>

    );

}