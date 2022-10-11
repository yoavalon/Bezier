d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.curve(Direction.S, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.short, Radius.high)
d.position_pen(1,2)

d.end()
