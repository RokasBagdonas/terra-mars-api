<template>
  <div class="field">
    <label class="label" v-if="label"> {{ label }}</label>

    <div class="control">
      <select
        :value="modelValue"
        class="select is-rounded"
        v-bind="$attrs"
        @change="$emit('update:modelValue', $event.target.value)"
      >
        <option
          v-for="option in options"
          :value="option"
          :key="option"
          :selected="option === modelValue"
        >
          {{ option[displayProp] }}
        </option>
      </select>
    </div>
  </div>
</template>


<script>
export default {
  props: {
    label: {
      type: String,
      default: "",
    },
displayProp: {
  type: String,
  default: "",
             },
    modelValue: {
      type: Object,
      default: null,
    },
    options: {
      type: Array,
      required: true,
    },
  },
};
</script>
