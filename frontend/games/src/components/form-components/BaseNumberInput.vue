<template>
  <div class="field">
    <label class="label" v-if="label"> {{ label }}</label>
    <div class="control">
      <div class="input is-primary">
        <input
          :placeholder="label"
          class="input"
          :value="modelValue"
          v-bind="$attrs"
          @input="$emit('update:modelValue', +$event.target.value)"
        />
      </div>
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
    modelValue: {
      type: [Number],
      default: "",
    },
  },
};
</script>
