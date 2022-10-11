d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.S, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,2)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)

d.end()
