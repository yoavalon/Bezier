d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.W, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.SW, Length.short)
d.position_pen(2,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)

d.end()
