d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.NW, Length.short)
d.position_pen(1,1)
d.curve(Direction.W, Orient.left, Length.long, Radius.high)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SW, Length.medium)

d.end()
