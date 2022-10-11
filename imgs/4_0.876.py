d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.SW, Orient.left, Length.short, Radius.low)
d.position_pen(2,1)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)

d.end()
