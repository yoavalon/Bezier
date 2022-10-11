d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.S, Orient.left, Length.short, Radius.low)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.NW, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.E, Length.medium)
d.position_pen(1,0)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)

d.end()
