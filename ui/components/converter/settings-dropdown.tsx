import { Dropdown, DropdownTrigger, DropdownMenu, DropdownSection, DropdownItem } from "@nextui-org/dropdown";
import { Button } from "@nextui-org/button";
import { Slider } from "@nextui-org/slider";
import { Select, SelectItem } from "@nextui-org/select";
import { CogFilledIcon } from "../icons";
import { Switch, } from "@nextui-org/switch"
import React from "react";

export default function SettingsDropdown({ videoFile, options, updateParam }) {

  const modelSizes = [
    { key: "tiny", label: "Tiny" },
    { key: "small", label: "Small" },
    { key: "medium", label: "Medium" },
    { key: "large", label: "Large" },
  ];

  const languages = [
    { key: "en", label: "English" },
    { key: "it", label: "Italian" },
    { key: "es", label: "Spanish" },
    { key: "pt", label: "Portuguese" },
  ];

  return (
    <>
      <Dropdown closeOnSelect={false} backdrop="blur">
        <DropdownTrigger>
          <Button isIconOnly color="default" isDisabled={!videoFile}>
            <CogFilledIcon className="text-default-500" />
          </Button>
        </DropdownTrigger>
        <DropdownMenu aria-label="Select settings">
          <DropdownSection title="Model language" showDivider>
            <DropdownItem key="model_size" textValue="model_size">
              <Select
                name="model_size"
                label="Select model size"
                selectedKeys={new Set([options.model_size])}
                value={options.model_size}
                onChange={(e) => updateParam('model_size', e.target.value)}
              >
                {modelSizes.map((modelSize) => (
                  <SelectItem key={modelSize.key} textValue={modelSize.label}>
                    {modelSize.label}
                  </SelectItem>
                ))}
              </Select>
            </DropdownItem>
            <DropdownItem key="language" textValue="language">
              <Select
                name="language"
                label="Select language"
                selectedKeys={new Set([options.language])}
                value={options.language}
                onChange={(e) => updateParam('language', e.target.value)}
              >
                {languages.map((lang) => (
                  <SelectItem key={lang.key} textValue={lang.label}>
                    {lang.label}
                  </SelectItem>
                ))}
              </Select>
            </DropdownItem>
          </DropdownSection>
          <DropdownSection title="Subtitles frequency" showDivider>

            <DropdownItem key="subtitles_frequency" textValue="settings">
              <Slider
                name="subtitles_frequency"
                label={`Subtitles frequency (s):  `}
                step={1}
                maxValue={50}
                minValue={0}
                value={options.subtitles_frequency}
                onChange={(e) => updateParam('subtitles_frequency', e)}
                className="max-w-md"
              />
            </DropdownItem>
          </DropdownSection>
          <DropdownSection title="Speaker detection">
            <DropdownItem key="speaker_detection" textValue="speaker_detection">
              <Switch isSelected={options.speaker_detection} onValueChange={(e) => updateParam('speaker_detection', e)}>
                Speaker detection
              </Switch>
            </DropdownItem>
          </DropdownSection>

        </DropdownMenu>
      </Dropdown>
    </>
  );
}
