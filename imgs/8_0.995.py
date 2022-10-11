d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,1)
d.curve(Direction.E, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)

d.end()
