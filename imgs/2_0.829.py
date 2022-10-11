d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.SW, Orient.left, Length.short, Radius.low)
d.curve(Direction.W, Orient.left, Length.short, Radius.high)
d.position_pen(2,2)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.E, Length.medium)

d.end()
