d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,1)
d.curve(Direction.W, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.NW, Orient.left, Length.short, Radius.medium)
d.position_pen(1,0)

d.end()
