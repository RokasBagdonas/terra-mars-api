<template>
  <div class="field">
    <label class="label" v-if="label"> {{ label }}</label>
    <div class="control">
    <input
      :placeholder="label"
      class="input"
      :value="modelValue"
      v-bind="$attrs"
      @input="$emit('update:modelValue', $event.target.value)"
    /></div>
  </div>
</template>


<script>
export default {
  props: {
    label: {
      type: String,
      default: "",
    },
    modelValue: {
      type: [String, Number],
      default: "",
    },
  },
};
</script>
