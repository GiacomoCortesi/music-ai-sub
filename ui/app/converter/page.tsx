import { title } from "@/components/primitives";
import Converter from "@/components/converter/converter";

export default function ConverterPage({ searchParams }) {
  return (
    <>
      <h1 className={title()}>MAIS Converter</h1>
      <p className="text-lg">
        Instantly create and edit subtitles from a music video
      </p>
      <Converter searchParams={searchParams} />
    </>
  );
}
