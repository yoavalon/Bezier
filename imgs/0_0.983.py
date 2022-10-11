d = DslBezier()

d.position_pen(0,3)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(2,1)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)

d.end()
