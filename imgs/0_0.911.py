d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(0,0)
d.straight_line(Direction.NW, Length.long)

d.end()
